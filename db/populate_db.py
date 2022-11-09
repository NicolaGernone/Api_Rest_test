from django.db.utils import DataError
from .csv_reader import read_csv
from api.infrastructure.models import Coin

def db_load(path):
    """Populate the DB with csv records."""
    try:
        data = read_csv(path)        
        for d in data:
            records, created = Coin.objects.get_or_create(
                sno=d[0],
                name=d[1],
                symbol=d[2],
                date=d[3],
                hight=d[4],
                low=d[5],
                open=d[6],
                close=d[7],
                volume=d[8],
                marketcap=d[9]
                )
                                                            
    except DataError as e:
        raise DataError(e)
