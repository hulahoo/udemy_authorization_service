from django.db import models

from commons.constants import NO_AUDIENCE, SMALL_AUDIENCE, BIG_AUIDENCE


class MentorInformation(models.Model):

    EDUCATION_AUDIENCE = (
        (NO_AUDIENCE, "No audience"),
        (SMALL_AUDIENCE, "Small audience"),
        (BIG_AUIDENCE, "Big audience")
    )

    previous_education_type = models.CharField(
        max_length=250
    )
    education_audience = models.CharField(
        choices=EDUCATION_AUDIENCE,
        default=NO_AUDIENCE
    )
