from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer

class LeaveRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Kullanıcının izin taleplerini getir
        leave_requests = LeaveRequest.objects.filter(employee__user=request.user)
        serializer = LeaveRequestSerializer(leave_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Yeni izin talebi oluştur
        serializer = LeaveRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee=request.user.employee)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
from django.shortcuts import render, redirect
from .models import LeaveRequest

def admin_dashboard(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'admin_dashboard.html', {'leave_requests': leave_requests})

def approve_leave(request, leave_id):
    leave = LeaveRequest.objects.get(id=leave_id)
    leave.status = 'Approved'
    leave.save()
    return redirect('admin_dashboard')

def reject_leave(request, leave_id):
    leave = LeaveRequest.objects.get(id=leave_id)
    leave.status = 'Rejected'
    leave.save()
    return redirect('admin_dashboard')
