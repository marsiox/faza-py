from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers.quotation_serializer import QuotationSerializer

class QuotationAPIView(APIView):
    def get(self, request):
        serializer = QuotationSerializer(data=request.query_params)

        if serializer.is_valid():
            print(serializer.validated_data)
            rooms = serializer.validated_data['rooms']
            sockets = serializer.validated_data['sockets']
            lights = serializer.validated_data['lights']
            phases = serializer.validated_data['phases']
            has_washing_machine = serializer.validated_data['has_washing_machine']
            has_induction = serializer.validated_data['has_induction']
            has_fridge = serializer.validated_data['has_fridge']
            has_dryer = serializer.validated_data['has_dryer']
            priceBreakdown = self.calculate_price_breakdown(rooms, sockets, lights, phases, has_washing_machine, has_induction, has_fridge, has_dryer)

            return Response({'priceBreakdown': priceBreakdown}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def calculate_price_breakdown(self, rooms, sockets, lights, phases, has_washing_machine, has_induction, has_fridge, has_dryer):
        # Define costs
        MEASUREMENT_COST = 300
        CIRCUIT_BREAKER_COST = 18
        AVG_CABLE_COST = 5
        LABOUR_PER_POINT_COST = 145

        # Calculate cable length
        total_cable_length = rooms * 25
        cables_cost = total_cable_length * AVG_CABLE_COST
        hardware_cost = cables_cost + ((sockets + lights) * 22)

        # Calculate costs
        extra_circuits = 0
        if has_washing_machine:
            extra_circuits += 1
        if has_induction:
            extra_circuits += 1
        if has_fridge:
            extra_circuits += 1
        if has_dryer:
            extra_circuits += 1

        extra_circuits_cost = extra_circuits * 200

        # Calculate circuits
        circuits = rooms * 2 + extra_circuits

        circuit_breakers_cost = circuits * CIRCUIT_BREAKER_COST
        rcds_cost = (200 * phases) + 300
        labour_cost = (sockets + lights) * LABOUR_PER_POINT_COST

        distribution_board_cost = circuit_breakers_cost + rcds_cost + 600

        total_cost = (
            extra_circuits_cost +
            MEASUREMENT_COST +
            distribution_board_cost +
            hardware_cost +
            labour_cost
        )
        print(extra_circuits)
        return {
            'extra_circuits_cost': extra_circuits_cost,
            'measurement_cost': MEASUREMENT_COST,
            'distribution_board_cost': distribution_board_cost,
            'labour_cost': labour_cost,
            'hardware_cost': hardware_cost,
            'total_cost': total_cost,
        }
