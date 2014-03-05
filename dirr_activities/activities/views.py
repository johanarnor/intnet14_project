from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from activities.models import Activity, Feature, FeatureOption


@login_required
def view_activity(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    features = activity.feature_set.all()
    # options = features.featureOption_set.all()
    # print options
    return render(request, 'activities/main.html', {'activity': activity, 'features': features})