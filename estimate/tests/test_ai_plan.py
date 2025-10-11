from __future__ import annotations

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch

from estimate.agentkit.project_planner import plan_project_schedule
from estimate.models import Project


class ProjectPlannerTests(TestCase):
    def test_schedule_orders_tasks_by_phase(self) -> None:
        payload = {
            "project": {"id": 1, "name": "Demo", "zip": "12345"},
            "slots": [
                {"id": "day-1", "label": "Day 1"},
                {"id": "day-2", "label": "Day 2"},
                {"id": "day-3", "label": "Day 3"},
                {"id": "day-4", "label": "Day 4"},
                {"id": "day-5", "label": "Day 5"},
                {"id": "day-6", "label": "Day 6"},
                {"id": "day-7", "label": "Day 7"},
            ],
            "timeline": {},
            "unscheduledTaskIds": ["t1", "t2", "t3"],
            "tasks": [
                {
                    "id": "t1",
                    "title": "Interior demolition",
                    "category": "demolition",
                    "estimateTitle": "",
                    "jobTitle": None,
                    "jobId": 101,
                    "resultId": 201,
                    "quantity": None,
                    "unitPrice": None,
                    "totalCost": None,
                    "unit": None,
                    "materials": [],
                    "meta": {},
                },
                {
                    "id": "t2",
                    "title": "Hang drywall",
                    "category": "drywall",
                    "estimateTitle": "",
                    "jobTitle": None,
                    "jobId": 101,
                    "resultId": 201,
                    "quantity": None,
                    "unitPrice": None,
                    "totalCost": None,
                    "unit": None,
                    "materials": [],
                    "meta": {},
                },
                {
                    "id": "t3",
                    "title": "Prime walls",
                    "category": "painting",
                    "estimateTitle": "",
                    "jobTitle": None,
                    "jobId": 101,
                    "resultId": 201,
                    "quantity": None,
                    "unitPrice": None,
                    "totalCost": None,
                    "unit": None,
                    "materials": [],
                    "meta": {},
                },
            ],
        }

        result = plan_project_schedule(payload)

        self.assertEqual(result.get("unscheduled"), [])
        timeline = result.get("timeline") or {}
        self.assertIn("day-1", timeline)
        self.assertIn("day-2", timeline)
        self.assertIn("day-4", timeline)

        self.assertEqual(timeline["day-1"][0]["taskId"], "t1")
        self.assertEqual(timeline["day-2"][0]["taskId"], "t2")
        self.assertEqual(timeline["day-2"][0]["durationDays"], 2)
        self.assertEqual(timeline["day-4"][0]["taskId"], "t3")
        slots = result.get("slots", [])
        self.assertEqual(len(slots), len(payload["tasks"]))
        self.assertEqual(slots[0]["label"], "Day 1")
        self.assertEqual(slots[0]["display"], "Day 1")


class AiPlanEndpointTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            username="planner",
            email="planner@example.com",
            password="pass1234",
        )
        self.project = Project.objects.create(name="Main House", zip="30301", owner=self.user)
        self.client.force_authenticate(self.user)

    @patch("estimate.views.generate_project_plan_with_ai")
    def test_ai_plan_endpoint_schedules_unscheduled_tasks(self, mock_agent) -> None:
        agent_plan = {
            "timeline": {
                "day-1": [{"taskId": "locked-1", "durationDays": 1}],
                "day-2": [{"taskId": "t-alpha", "durationDays": 2}],
            },
            "unscheduled": ["t-beta"],
            "notes": "Drywall follows site prep.",
            "slots": [
                {"id": "day-1", "label": "Day 1"},
                {"id": "day-2", "label": "Day 2"},
            ],
        }
        mock_agent.return_value = agent_plan

        payload = {
            "project": {"id": self.project.pk, "name": self.project.name, "zip": self.project.zip},
            "slots": [
                {"id": "day-1", "label": "Day 1"},
                {"id": "day-2", "label": "Day 2"},
                {"id": "day-3", "label": "Day 3"},
            ],
            "timeline": {"day-1": ["locked-1"]},
            "unscheduledTaskIds": ["t-alpha", "t-beta"],
            "tasks": [
                {
                    "id": "locked-1",
                    "title": "Dumpster delivery",
                    "category": "site_cleanup",
                    "estimateTitle": "",
                    "jobTitle": None,
                    "jobId": 1,
                    "resultId": 1,
                    "quantity": None,
                    "unitPrice": None,
                    "totalCost": None,
                    "unit": None,
                    "materials": [],
                    "meta": {"durationDays": 1, "status": "planned"},
                },
                {
                    "id": "t-alpha",
                    "title": "Hang drywall",
                    "category": "drywall",
                    "estimateTitle": "",
                    "jobTitle": None,
                    "jobId": 1,
                    "resultId": 1,
                    "quantity": None,
                    "unitPrice": None,
                    "totalCost": None,
                    "unit": None,
                    "materials": [],
                    "meta": {},
                },
                {
                    "id": "t-beta",
                    "title": "Prime walls",
                    "category": "painting",
                    "estimateTitle": "",
                    "jobTitle": None,
                    "jobId": 1,
                    "resultId": 1,
                    "quantity": None,
                    "unitPrice": None,
                    "totalCost": None,
                    "unit": None,
                    "materials": [],
                    "meta": {},
                },
            ],
        }

        response = self.client.post(
            f"/api/projects/{self.project.pk}/ai-plan/",
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["X-Plan-Source"], "ai")
        data = response.json()
        self.assertEqual(data, agent_plan)

        self.project.refresh_from_db()
        self.assertEqual(self.project.plan_ai_response, agent_plan)
        payload_slots = self.project.plan_ai_payload.get("slots")
        self.assertTrue(payload_slots)
        self.assertEqual(len(payload_slots), len(payload["tasks"]))
        self.assertEqual(payload_slots[0]["label"], "Day 1")
        self.assertEqual(payload_slots[0].get("display"), "Day 1")
        self.assertIsNotNone(self.project.plan_ai_updated)

    @patch("estimate.views.generate_project_plan_with_ai", side_effect=RuntimeError("boom"))
    def test_ai_plan_endpoint_falls_back_to_heuristic(self, mock_agent) -> None:
        payload = {
            "project": {"id": self.project.pk, "name": self.project.name, "zip": self.project.zip},
            "slots": [
                {"id": "day-1", "label": "Day 1"},
                {"id": "day-2", "label": "Day 2"},
                {"id": "day-3", "label": "Day 3"},
            ],
            "timeline": {},
            "unscheduledTaskIds": ["a", "b"],
            "tasks": [
                {
                    "id": "a",
                    "title": "Demo",
                    "category": "demolition",
                    "estimateTitle": "",
                    "jobTitle": None,
                    "jobId": 1,
                    "resultId": 1,
                    "quantity": None,
                    "unitPrice": None,
                    "totalCost": None,
                    "unit": None,
                    "materials": [],
                    "meta": {},
                },
                {
                    "id": "b",
                    "title": "Drywall",
                    "category": "drywall",
                    "estimateTitle": "",
                    "jobTitle": None,
                    "jobId": 1,
                    "resultId": 1,
                    "quantity": None,
                    "unitPrice": None,
                    "totalCost": None,
                    "unit": None,
                    "materials": [],
                    "meta": {},
                },
            ],
        }

        response = self.client.post(
            f"/api/projects/{self.project.pk}/ai-plan/",
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["X-Plan-Source"], "fallback")
        data = response.json()
        self.assertIn("timeline", data)
        self.assertIn("unscheduled", data)
        self.assertIn("slots", data)
        self.assertEqual(len(data.get("slots", [])), len(payload["tasks"]))
        self.project.refresh_from_db()
        self.assertEqual(self.project.plan_ai_response, data)

    def test_ai_plan_endpoint_manual_save(self) -> None:
        payload = {
            "project": {"id": self.project.pk, "name": self.project.name, "zip": self.project.zip},
            "slots": [
                {"id": "day-1", "label": "Day 1", "display": "Day 1", "order": 1},
                {"id": "day-2", "label": "Day 2", "display": "Day 2", "order": 2},
            ],
            "timeline": {"day-1": ["a"]},
            "unscheduledTaskIds": ["b"],
            "tasks": [
                {
                    "id": "a",
                    "title": "Demo work",
                    "category": "demolition",
                    "estimateTitle": "",
                    "jobTitle": None,
                    "jobId": 1,
                    "resultId": 1,
                    "quantity": None,
                    "unitPrice": None,
                    "totalCost": None,
                    "unit": None,
                    "materials": [],
                    "meta": {"durationDays": 2, "startSlot": "day-1", "status": "In progress"},
                },
                {
                    "id": "b",
                    "title": "Drywall",
                    "category": "drywall",
                    "estimateTitle": "",
                    "jobTitle": None,
                    "jobId": 1,
                    "resultId": 1,
                    "quantity": None,
                    "unitPrice": None,
                    "totalCost": None,
                    "unit": None,
                    "materials": [],
                    "meta": {},
                },
            ],
        }

        plan = {
            "timeline": {
                "day-1": [
                    {
                        "taskId": "a",
                        "durationDays": 2,
                        "status": "In progress",
                        "notes": "demo first",
                    }
                ]
            },
            "unscheduled": ["b"],
            "notes": "Manual adjustment",
            "slots": payload["slots"],
        }

        response = self.client.patch(
            f"/api/projects/{self.project.pk}/ai-plan/",
            {"payload": payload, "plan": plan},
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["X-Plan-Source"], "manual")
        saved_plan = response.json()
        self.assertIn("timeline", saved_plan)
        self.assertIn("slots", saved_plan)
        self.assertEqual(len(saved_plan["slots"]), len(payload["slots"]))

        self.project.refresh_from_db()
        self.assertEqual(self.project.plan_ai_response, saved_plan)
        self.assertEqual(self.project.plan_ai_payload, payload)
