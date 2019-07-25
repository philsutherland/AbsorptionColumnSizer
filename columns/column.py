from exceptions.could_not_construct_object_exception import CouldNotConstructObjectException
from exceptions.range_limit_exception import RangeLimitException


class Column:
    def __init__(self, num_step, percent_recovery, packing_type):

        # Check if input values are in acceptable range
        if(num_step_in_range_check(num_step) and percent_recovery_in_range_check(percent_recovery) and packing_type_in_range_check(packing_type)):
            self.num_step = num_step
            self.percent_recovery = percent_recovery/100
            self.packing_type = packing_type
            self.column_diam = 435
            self.column_area = 23
        else:
            raise CouldNotConstructObjectException("Column")
