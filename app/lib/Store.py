import os
import json
import time
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

class Store():
    def __init__(self):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'sanibid.db')
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(file_path)
        self.initialize()
        
    def initialize(self):
        start_time = time.time()
        if self.db.open():
            print("open DB success")
            if not self.db.tables():
                print( "No tables found")
                self.createTables()
                self.importCountries()
                self.importMaterials()
                self.importInspectionDevices()
                self.importPipes()
                self.importCriterias()
                self.makeDefaultRelations()
                self.db.close()
            else:
                print("Tables already exist")                
        else:
            print("Error openind database")
        print("Total time execution to initialize: --- %s seconds ---" % (time.time() - start_time))

    def createTables(self):
        print("Creating Tables ...")
        query = QSqlQuery()
 
        query.exec_("CREATE TABLE IF NOT EXISTS countries\
            (id integer primary key autoincrement,\
            name_en text unique not null,\
            name_es text unique not null,\
            name_pt text unique not null,\
            iso2 text)")

        query.exec_("CREATE TABLE IF NOT EXISTS materials\
            (id integer primary key autoincrement,\
            name_en text,\
            name_es text,\
            name_pt text,\
            min_diameter double precision,\
            max_diameter double precision,\
            manning_roughness_c double precision,\
            created_at datetime,\
            updated_at datetime)")

        query.exec_("CREATE TABLE IF NOT EXISTS project_criterias\
            (id integer primary key autoincrement,\
            name text unique not null,\
            water_consumption_pc double precision,\
            k1_daily double precision,\
            k2_hourly double precision,\
            coefficient_return_c double precision,\
            intake_rate double precision,\
            avg_tractive_force_min double precision,\
            flow_min_qmin double precision,\
            water_surface_max double precision,\
            max_water_level double precision,\
            min_diameter double precision,\
            diameter_up_150 double precision,\
            diameter_up_200 double precision,\
            from_diameter_250 double precision,\
            cover_min_street double precision,\
            cover_min_sidewalks_gs double precision,\
            type_preferred_head_col text,\
            max_drop double precision,\
            bottom_ib_mh double precision,\
            created_at datetime,\
            updated_at datetime)")

        query.exec_("CREATE TABLE IF NOT EXISTS parameters\
            (id integer primary key autoincrement,\
            project_criteria_id integer not null,\
            layer_name text,\
            final_population integer,\
            beginning_population integer,\
            occupancy_rate_start double precision,\
            occupancy_rate_end double precision,\
            residences_end integer,\
            residences_start integer,\
            connections_end integer,\
            connections_start integer,\
            point_flows_end double precision,\
            point_flows_start double precision,\
            qe_reference_max double precision,\
            qe_reference_med double precision,\
            contribution_sewage boolean,\
            sewer_contribution_rate_end double precision,\
            sewer_contribution_rate_start double precision,\
            created_at datetime,\
            updated_at datetime,\
            FOREIGN KEY(project_criteria_id) REFERENCES project_criterias(id))")

        query.exec_("CREATE TABLE IF NOT EXISTS projects\
            (id integer primary key autoincrement,\
            parameter_id integer,\
            name text unique not null,\
            country_id integer,\
            city text,\
            microsystem text,\
            author text,\
            active boolean,\
            date date,\
            created_at datetime,\
            updated_at datetime,\
            FOREIGN KEY(parameter_id) REFERENCES parameters(id),\
            FOREIGN KEY(country_id) REFERENCES countries(id))")
     
        query.exec_("CREATE TABLE IF NOT EXISTS pipes\
            (id integer primary key autoincrement,\
            diameter double precision,\
            material_id integer,\
            manning_suggested double precision,\
            manning_adopted double precision,\
            created_at datetime,\
            updated_at datetime,\
            FOREIGN KEY(material_id) REFERENCES materials(id))")

        query.exec_("CREATE TABLE IF NOT EXISTS criterias_pipes\
            (id integer primary key autoincrement,\
            pipe_id integer,\
            criteria_id integer,\
            project_id integer,\
            created_at datetime,\
            updated_at datetime,\
            FOREIGN KEY(pipe_id) REFERENCES pipes(id),\
            FOREIGN KEY(criteria_id) REFERENCES project_criterias(id),\
            FOREIGN KEY(project_id) REFERENCES projects(id))")

        query.exec_("CREATE TABLE IF NOT EXISTS inspection_devices\
            (id integer primary key autoincrement,\
            type_en text,\
            type_es text,\
            type_pt text,\
            max_depth double precision,\
            max_diameter_suggested double precision,\
            created_at datetime,\
            updated_at datetime)")

        query.exec_("CREATE TABLE IF NOT EXISTS criterias_inspection_devices\
            (id integer primary key autoincrement,\
            inspection_devices_id integer,\
            criteria_id integer,\
            project_id integer,\
            created_at datetime,\
            updated_at datetime,\
            FOREIGN KEY(inspection_devices_id) REFERENCES inspection_devices(id),\
            FOREIGN KEY(criteria_id) REFERENCES project_criterias(id),\
            FOREIGN KEY(project_id) REFERENCES projects(id))")
        
        query.exec_("CREATE TABLE IF NOT EXISTS calculations\
            (id integer primary key autoincrement,\
            project_id integer,\
            layer_name text,\
            initial_segment boolean,\
            final_segment boolean,\
            collector_number integer,\
            col_seg text,\
            extension double precision,\
            previous_col_seg_id text,\
            m1_col_id text,\
            m2_col_id text,\
            block_others_id text,\
            qty_final_qe integer,\
            qty_initial_qe integer,\
            intake_in_seg double precision,\
            total_flow_rate_end double precision,\
            total_flow_rate_start double precision,\
            col_pipe_position integer,\
            aux_prof_i text,\
            force_depth_up double precision,\
            aux_depth_adjustment double precision,\
            covering_up double precision,\
            covering_down double precision,\
            depth_up double precision,\
            depth_down double precision,\
            force_depth_down double precision,\
            el_terr_up double precision,\
            el_terr_down double precision,\
            el_col_up double precision,\
            el_col_down double precision,\
            el_top_gen_up double precision,\
            el_top_gen_down double precision,\
            slopes_terr double precision,\
            slopes_min_accepted_col double precision,\
            slopes_adopted_col double precision,\
            suggested_diameter double precision,\
            adopted_diameter double precision,\
            c_manning double precision,\
            prj_flow_rate_qgmax double precision,\
            water_level_pipe_end double precision,\
            tractive_force double precision,\
            critical_velocity double precision,\
            velocity double precision,\
            initial_flow_rate_qi double precision,\
            water_level_ipe_start double precision,\
            tractive_foce_start double precision,\
            inspection_id_up text,\
            inspection_type_up text,\
            inspection_id_down text,\
            inspection_type_down text,\
            downstream_seg_id text,\
            observations text,\
            created_at datetime,\
            updated_at datetime,\
            FOREIGN KEY(project_id) REFERENCES projects(id))")
        
        query.exec_("CREATE TABLE IF NOT EXISTS contributions\
            (id integer primary key autoincrement,\
            calculation_id integer,\
            col_seg text,\
            previous_col_seg_end double precision,\
            col_pipe_m1_end double precision,\
            col_pipe_m2_end double precision,\
            subtotal_up_seg_end double precision,\
            condominial_lines_end double precision,\
            linear_contr_seg_end double precision,\
            previous_col_seg_start double precision,\
            col_pipe_m1_start double precision,\
            col_pipe_m2_start double precision,\
            subtotal_up_seg_start double precision,\
            condominial_lines_start double precision,\
            linear_contr_seg_start double precision,\
            created_at datetime,\
            updated_at datetime,\
            FOREIGN KEY(calculation_id) REFERENCES calculations(id))")

        query.exec_("CREATE TABLE IF NOT EXISTS wl_adjustments\
            (id integer primary key autoincrement,\
            calculation_id integer,\
            col_seg text,\
            previous_col_seg_end text,\
            created_at datetime,\
            updated_at datetime,\
            FOREIGN KEY(calculation_id) REFERENCES calculations(id))")

    def importCountries(self):
        print("Inserting Countries.")
        query = QSqlQuery()
        filename = os.path.join(os.path.dirname(__file__), '..', 'data', 'countries.json')
        with open(filename) as json_file:
            countries = json.load(json_file)
        values = ''
        for p in countries:
            values += "('"+p['name_en']+"','"+p['name_es']+"','"+p['name_pt']+"','"+p['iso2']+"'),"
        execQuery = "INSERT INTO countries (name_en, name_es, name_pt, iso2) VALUES "+ values[:-1] + ";"
        query.exec_('BEGIN TRANSACTION;')
        query.exec_(execQuery)
        query.exec_('COMMIT;')
        print("Finalizing Country table")

    def importMaterials(self):
        print("Inserting Materials.")
        query = QSqlQuery()
        filename = os.path.join(os.path.dirname(__file__), '..', 'data', 'materials.json')
        with open(filename) as json_file:
            materials = json.load(json_file)
        values = ''
        for p in materials:
            values += "('"+p['name_en']+"','"+p['name_es']+"','"+p['name_pt']+"','"+str(p['min_diameter'])+"','"+str(p['max_diameter'])+"',\
                        '"+str(p['manning_roughness_c'])+"', datetime('now'), datetime('now')),"
        execQuery = "INSERT INTO materials (name_en, name_es, name_pt, min_diameter, max_diameter,\
                        manning_roughness_c, created_at, updated_at) VALUES "+ values[:-1] + ";"
        query.exec_('BEGIN TRANSACTION;')
        query.exec_(execQuery)
        query.exec_('COMMIT;')
        print("Finalizing Materials table")

    def importInspectionDevices(self):
        print("Inserting Inspection Devices.")
        query = QSqlQuery()
        filename = os.path.join(os.path.dirname(__file__), '..', 'data', 'inspection-devices.json')
        with open(filename) as json_file:
            inspection_devices = json.load(json_file)
        values = ''
        for p in inspection_devices:
            values += "('"+p['type_en']+"','"+p['type_es']+"','"+p['type_pt']+"','"+str(p['max_depth'])+"',\
                        '"+str(p['max_diameter_suggested'])+"', datetime('now'), datetime('now')),"
        execQuery = "INSERT INTO inspection_devices (type_en, type_es, type_pt, max_depth,  max_diameter_suggested, created_at, updated_at) VALUES "+ values[:-1] + ";"
        query.exec_('BEGIN TRANSACTION;')
        query.exec_(execQuery)
        query.exec_('COMMIT;')
        print("Finalizing Inspection Devices table")
    
    def importPipes(self):
        print("Inserting Pipes.")
        query = QSqlQuery()
        filename = os.path.join(os.path.dirname(__file__), '..', 'data', 'pipes.json')
        with open(filename) as json_file:
            pipes = json.load(json_file)
        values = ''
        for p in pipes:
            values += "('"+str(p['diameter'])+"','"+str(p['material_id'])+"','"+str(p['manning_suggested'])+"','"+str(p['manning_adopted'])+"',\
                        datetime('now'), datetime('now')),"
        execQuery = "INSERT INTO pipes (diameter, material_id, manning_suggested, manning_adopted, created_at, updated_at) VALUES "+ values[:-1] + ";"
        query.exec_('BEGIN TRANSACTION;')
        query.exec_(execQuery)
        query.exec_('COMMIT;')
        print("Finalizing Pipes table")

    def importCriterias(self):
        print("Inserting SANIBID Criterias.")
        query = QSqlQuery()
        filename = os.path.join(os.path.dirname(__file__), '..', 'data', 'criterias.json')
        with open(filename) as json_file:
            criterias = json.load(json_file)
        values = ''
        for p in criterias:
            values += "('"+p['name']+"','"+p['water_consumption_pc']+"','"+p['k1_daily']+"','"+p['k2_hourly']+"','"+p['coefficient_return_c']+"',\
                '"+p['intake_rate']+"','"+p['avg_tractive_force_min']+"','"+p['flow_min_qmin']+"','"+p['water_surface_max']+"','"+p['max_water_level']+"',\
                '"+p['min_diameter']+"','"+p['diameter_up_150']+"','"+p['diameter_up_200']+"','"+p['from_diameter_250']+"','"+p['cover_min_street']+"',\
                '"+p['cover_min_sidewalks_gs']+"','"+p['type_preferred_head_col']+"','"+p['max_drop']+"','"+p['bottom_ib_mh']+"', datetime('now'), datetime('now')),"

        execQuery = "INSERT INTO project_criterias (name, water_consumption_pc, k1_daily, k2_hourly, coefficient_return_c, intake_rate, \
            avg_tractive_force_min, flow_min_qmin, water_surface_max, max_water_level, min_diameter, diameter_up_150, diameter_up_200, \
            from_diameter_250, cover_min_street, cover_min_sidewalks_gs, type_preferred_head_col, max_drop, bottom_ib_mh, \
            created_at, updated_at) VALUES "+ values[:-1] + ";"

        query.exec_('BEGIN TRANSACTION;')
        query.exec_(execQuery)
        query.exec_('COMMIT;')
        print("Finalizing Project_Criterias table")
    
    def makeDefaultRelations(self):
        print("Inserting Default Relations.")
        query = QSqlQuery()
        query.exec_('BEGIN TRANSACTION;')
        execQuery = "INSERT into criterias_pipes(pipe_id, criteria_id,created_at,updated_at)\
                        VALUES (1, 1,datetime('now'),datetime('now')),\
                        (2,1,datetime('now'),datetime('now')),\
                        (3,1,datetime('now'),datetime('now')),\
                        (4,1,datetime('now'),datetime('now')),\
                        (5,1,datetime('now'),datetime('now')),\
                        (6,1,datetime('now'),datetime('now')),\
                        (7,1,datetime('now'),datetime('now')),\
                        (8,1,datetime('now'),datetime('now')),\
                        (9,1,datetime('now'),datetime('now')),\
                        (10,1,datetime('now'),datetime('now')),\
                        (11,1,datetime('now'),datetime('now')),\
                        (12,1,datetime('now'),datetime('now')),\
                        (13,1,datetime('now'),datetime('now')),\
                        (14,1,datetime('now'),datetime('now'));"
        query.exec_(execQuery)
        query.exec_('COMMIT;')

        query.exec_('BEGIN TRANSACTION;')
        execQuery = "INSERT into criterias_inspection_devices (inspection_devices_id, criteria_id,created_at,updated_at)\
                        VALUES (1, 1,datetime('now'),datetime('now')),\
                        (2,1,datetime('now'),datetime('now')),\
                        (3,1,datetime('now'),datetime('now')),\
                        (4,1,datetime('now'),datetime('now')),\
                        (5,1,datetime('now'),datetime('now')),\
                        (6,1,datetime('now'),datetime('now'));"
        query.exec_(execQuery)
        query.exec_('COMMIT;')
        print("Finalizing Default Relations")

    def getDB(self):
        return self.db