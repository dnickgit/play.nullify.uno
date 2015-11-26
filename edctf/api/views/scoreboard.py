from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from edctf.api.models import scoreboard, team
from edctf.api.serializers import scoreboardSerializer, teamSerializer
import time


class scoreboardView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, id=None, format=None):
        """
        Get all scoreboards or get by id via scoreboards/:id
        """
        # If scoreboard id was requested return that scoreboard else return list of scoreboards
        if id:
            # Retrieve and serialize the requested scoreboard data
            scoreboards = scoreboard.objects.filter(id=id)
            scoreboards_serializer = scoreboardSerializer(scoreboards, many=True, context={'request': request})
            
            # Retrieve and serialize the teams on the scoreboard
            teams = team.objects.filter(scoreboard=scoreboards[0]).order_by('-points','-last_timestamp', 'id')
            teams_serializer = teamSerializer(teams, many=True, context={'request': request})
            for pos,t in enumerate(teams_serializer.data):
                t['position'] = pos+1

            # Return the serialized data
            return Response({
                "scoreboards": scoreboards_serializer.data,
                "teams": teams_serializer.data,
            })

        else:
            # Retrieve and serialize the requested scoreboard data
            scoreboards = scoreboard.objects.all()
            scoreboards_serializer = scoreboardSerializer(scoreboards, many=True, context={'request': request})

            # Return the serialized data
            return Response({
                "scoreboards": scoreboards_serializer.data,
            })
