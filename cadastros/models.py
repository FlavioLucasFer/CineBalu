from django.db import models

class Room(models.Model):
    class RowsIndexStrategy(models.TextChoices):
        NUMERIC = 'NR', ('Numeric')
        ALPHA = 'AP', ('Alphabetic')

    seat_rows_index_strategy = models.CharField(
        max_length=2,
        choices=RowsIndexStrategy.choices,
        default=RowsIndexStrategy.ALPHA,
        verbose_name="Seat rows are numeric or alphabetic named?",
    )
    sound_tecnology = models.CharField()
    image_tecnology = models.CharField()
    emergency_exits = models.PositiveSmallIntegerField(verbose_name="How many emergency exits does the room have?")


class SeatRow(models.Model):
    index = models.CharField(max_length=3)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

class Seat(models.Model):
    class SeatTypes(models.TextChoices):
        NORMAL = 'NM', ('Normal')
        VIP = 'VP', ('VIP')
        WEELCHAIR = 'WC', ('Weelchair')

    type = models.CharField(
        max_length=2,
        choices=SeatTypes.choices,
        default=SeatTypes.NORMAL,
    )
    status = models.BooleanField(default=True)
    seat_row = models.ForeignKey(SeatRow, on_delete=models.CASCADE)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    director = models.CharField(max_length=150)
    cast = models.CharField(max_length=500)

class Showtime(models.Model):
    class ShowtimeTypes(models.TextChoices):
        TWO_D = '2D', ('2D')
        THREE_D = '3D', ('3D')
        SUBTITLED_2D = 'S2', ('Subtitled/2D')
        SUBTITLED_3D = 'S3', ('Subtitled/3D')

    time = models.TimeField()
    type = models.CharField(
        max_length=2,
        choices=ShowtimeTypes.choices,
        default=ShowtimeTypes.TWO_D,
    )
    price = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.BooleanField(default=True)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)

class Ticket(models.Model):
    class TicketType(models.TextChoices):
        HALF = 'H', ('Half')
        FULL = 'F', ('Full')

    price = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField()
    type = models.CharField(
        max_length=1,
        choices=TicketType.choices,
        default=TicketType.FULL,
    )
    showtime = models.ForeignKey(Showtime, on_delete=models.PROTECT)
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT)

