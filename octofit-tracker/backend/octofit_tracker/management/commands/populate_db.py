from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Hard'),
            Workout.objects.create(name='Strength Training', description='Build muscle', difficulty='Medium'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], workout=workouts[0], date=timezone.now().date(), duration_minutes=30, calories_burned=300)
        Activity.objects.create(user=users[1], workout=workouts[1], date=timezone.now().date(), duration_minutes=45, calories_burned=400)
        Activity.objects.create(user=users[2], workout=workouts[0], date=timezone.now().date(), duration_minutes=25, calories_burned=250)
        Activity.objects.create(user=users[3], workout=workouts[1], date=timezone.now().date(), duration_minutes=50, calories_burned=420)

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=300, rank=2)
        Leaderboard.objects.create(user=users[1], score=400, rank=1)
        Leaderboard.objects.create(user=users[2], score=250, rank=4)
        Leaderboard.objects.create(user=users[3], score=420, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
