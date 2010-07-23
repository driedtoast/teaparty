import sqlalchemy as sa
from sqlalchemy import MetaData
import sqlalchemy.orm as orm
import tp.models as models
import tp.utilize as utilize

initialized = False
engine = None
sm = None
cfg = None

# Global metadata. If you have multiple databases with overlapping table 
# names, you'll need a metadata for each database.
metadata = MetaData()

table_amis = sa.Table('amazon_images', metadata,
	sa.Column('amazon_id', sa.types.Text, primary_key=True),
	sa.Column('simple_name', sa.types.Text, nullable=False),
	sa.Column('kernel_id', sa.types.Text, nullable=True),
	sa.Column('ramdisk_id', sa.types.Text, nullable=True),
	sa.Column('os_type',sa.types.Text,nullable=True),	
	sa.Column('arch_type',sa.types.Text,nullable=True),
	sa.Column('added', sa.types.DateTime, nullable=False))

table_stereotypes = sa.Table('app_stereotypes', metadata,
	sa.Column('name', sa.types.Text, primary_key=True),
	sa.Column('added', sa.types.DateTime, nullable=False))

def initdb():
	global engine, sm, initialized, table_amis, metadata
	if(initialized == False):
		utilize.setupdata()		
		dburl = 'sqlite:///'+utilize.datadir +'/teaparty.sqlite'
		engine = sa.create_engine(dburl)
		print( ' engine is ' + str(engine) )
		metadata.create_all(engine)
		sm = orm.sessionmaker(autoflush=True, autocommit=True, bind=engine)
		orm.mapper(models.AmazonImage, table_amis)
		orm.mapper(models.AppStereoType, table_stereotypes)
		initialized = True

def session():
	session = sm()
	## session = orm.scoped_session(sm)
	return session


def check():
	return sa.__version__
