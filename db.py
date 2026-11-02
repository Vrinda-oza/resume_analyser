# DATABASE_URL = "mysql+mysqldb://4BBWaSEAsvcvK2M.root:cPauJwHAAwy6PIxE@gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com:4000/test?ssl_mode=VERIFY_IDENTITY&ssl_ca=C:/Users/Oza Vrinda/PycharmProjects/resume_analyser/isrgrootx1.pem/test"

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://4BBWaSEAsvcvK2M.root:cPauJwHAAwy6PIxE@gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com:4000/test"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ca": "C:/Users/Oza Vrinda/PycharmProjects/resume_analyser/isrgrootx1.pem"
        }
    }
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()