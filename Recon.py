class Recon:
    def __init__(self, sn, tn, c_cob_date, y_cob_date, c_count, y_count, r_type, r_value, remarks, p_date):
        self._source_name = sn
        self._table_name = tn
        self._previous_cob_date = y_cob_date
        self._current_cob_date = c_cob_date
        self._previous_count = y_count
        self._current_count = c_count
        self._remarks = remarks
        self._process_date = p_date
        self._recon_type = r_type
        self._recon_value = r_value

    def get_source_name(self):
        return self._source_name

    def get_table_name(self):
        return self._table_name

    def get_previous_cob_date(self):
        return self._previous_cob_date

    def get_current_cob_date(self):
        return  self._current_cob_date

    def get_previous_count(self):
        return self._previous_count

    def get_current_count(self):
        return self._current_count

    def get_remarks(self):
        return self._remarks

    def get_process_date(self):
        return self._process_date

    def get_recon_type(self):
        return self._recon_type

    def get_recon_value(self):
        return self._recon_value

    def __str__(self):
        return "source name is "+self._source_name + " table name is "+self._table_name + " current cob date is "+\
               self._current_cob_date + " previous cob date is "+self._previous_cob_date + " current count is " + self._current_count +\
               " previous count is " + self._previous_count + " remarks is "+self._remarks

    def __eq__(self, other):
        return (self._source_name == other._source_name) and \
               (self._table_name == other._table_name) and \
               self._recon_type == other._recon_type

    def __hash__(self):
        return hash(('_source_name', self._source_name, \
                     '_table_name', self._table_name, \
                     '_recon_type', self._recon_type))

