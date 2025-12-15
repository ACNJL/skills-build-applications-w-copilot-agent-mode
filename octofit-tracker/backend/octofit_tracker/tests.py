from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@test.com', team=team)
        self.assertEqual(str(user), 'U')
    def test_workout_create(self):
        workout = Workout.objects.create(name='W', description='d', difficulty='Easy')
        self.assertEqual(str(workout), 'W')
    def test_activity_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@test.com', team=team)
        workout = Workout.objects.create(name='W', description='d', difficulty='Easy')
        activity = Activity.objects.create(user=user, workout=workout, date='2025-01-01', duration_minutes=10, calories_burned=100)
        self.assertEqual(str(activity), 'U - W on 2025-01-01')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@test.com', team=team)
        lb = Leaderboard.objects.create(user=user, score=10, rank=1)
        self.assertEqual(str(lb), 'U - Rank 1')
