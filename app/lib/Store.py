import os
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

class Store():
    def __init__(self):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'sanibid.db')
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(file_path)
        self.initialize()
        
    def initialize(self):
        if self.db.open():
            print("open DB success")
            if not self.db.tables():
                print( "No tables found")
                self.createTables()
                self.db.close()
            else:
                print("Tables already exist")                
        else:
            print("Error openind database")

    def createTables(self):
        print("creating tables ...")
        query = QSqlQuery()
 
        query.exec_("CREATE TABLE IF NOT EXISTS countries\
            (id integer primary key autoincrement,\
            name text unique not null,\
            iso2 text)")

        query.exec_("CREATE TABLE IF NOT EXISTS materials\
            (id integer primary key autoincrement,\
            name text,\
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
            conver_min_sidewalks_gs double precision,\
            type_preferred_head_col text,\
            max_drop double precision,\
            bottom_ib_mh double precision,\
            created_at datetime,\
            updated_at datetime)")

        query.exec_("CREATE TABLE IF NOT EXISTS parameters\
            (id integer primary key autoincrement,\
            name text unique not null,\
            project_criteria_id integer,\
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
            type text,\
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
            previous_seg_id text,\
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

    def getDB(self):
        return self.db