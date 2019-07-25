class Column:
    def __init__(self, num_step, percent_recovery, packing_type):

        # Check if input values are in acceptable range
        if(num_step_in_range_check(num_step) and percent_recovery_in_range_check(percent_recovery) and packing_type_in_range_check(packing_type)):
            self.num_step = num_step
            self.percent_recovery = percent_recovery
            self.packing_type = packing_type
        else:
            raise
