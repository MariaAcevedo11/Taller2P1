import os
import csv
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Update images :D"

    def handle(self, *args, **kwargs):
        # 📥 Ruta del archivo CSV con las descripciones actualizadas
        updated_count = 0

    # 📖 Abrimos el CSV y leemos cada fila
        
        for movie in Movie.objects.all():
            if not os.path.exists("./media/movie/images/m_" + movie.title + ".png"):
                self.stderr.write(f"Image file  'm_{movie.title}.png' not found.")
            else:
                movie.image = "movie/images/m_" + movie.title + ".png"
                movie.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"Updated: {movie.title} image succesfully loaded"))

    # ✅ Al finalizar, muestra cuásntas películas se actualizaron
        self.stdout.write(self.style.SUCCESS(f"Finished updating {updated_count} movies image from Images Folder."))


    def specialCharacter(self): 
        ()