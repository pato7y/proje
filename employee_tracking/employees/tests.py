from django.test import TestCase
from .models import Employee, LeaveRequest

class LeaveRequestTestCase(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name="John Doe", email="john.doe@example.com")
        self.leave_request = LeaveRequest.objects.create(
            employee=self.employee,
            start_date="2024-12-01",
            end_date="2024-12-10",
            status="Pending"
        )

    def test_leave_approval(self):
        self.leave_request.status = 'Approved'
        self.leave_request.save()
        self.assertEqual(self.leave_request.status, 'Approved')
