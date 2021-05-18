from PyQt5.QtSql import (
    QSqlTableModel,
    QSqlQuery,
)


class Parameter(QSqlTableModel):
    def __init__(self, *args, **kwargs):
        super(Parameter, self).__init__(*args, **kwargs)
        self.setTable("parameters")
        self.select()

    def getValueBy(self, column, where=None):
        sql = "SELECT p.{}\
                FROM parameters p\
                LEFT JOIN projects pr ON p.id = pr.parameter_id\
                WHERE pr.active".format(
            column
        )
        if where != None:
            sql = sql + " AND {}".format(where)
        query = QSqlQuery(sql)
        if query.first():
            return query.value(0)
        else:
            return 0

    @staticmethod
    def lastInsertedId():
        # Todo: check if there is a better way to do this
        query = QSqlQuery("select max(id) from parameters")
        if query.first():
            return query.value(0)
        return None
