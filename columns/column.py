from exceptions.could_not_construct_object_exception import CouldNotConstructObjectException
from exceptions.range_limit_exception import RangeLimitException
from staticresources.constant import Constant as C
from formatting.formatted_text_menu import FormattedTextMenu as FTM


class Column:
    def __init__(self, num_step, percent_recovery, packing_type):

        # Check if input values are in acceptable range
        if(self.num_step_in_range_check(num_step) and self.percent_recovery_in_range_check(percent_recovery) and self.packing_type_in_range_check(packing_type)):
            self.__num_step = num_step
            self.__percent_recovery = percent_recovery/100
            self.__packing_type = packing_type
            self.__column_diam = 435
            self.__column_area = 23
        else:
            raise CouldNotConstructObjectException("Column")

    @classmethod
    def num_step_in_range_check(cls, num_step):
        if(num_step >= C.num_step_lower_limit and num_step <= C.num_step_upper_limit):
            return True
        else:
            C.clear()
            FTM.error_title(
                "Error: Number of numerical integration steps is out of acceptable range!")
            return False

    @classmethod
    def percent_recovery_in_range_check(cls, percent_recovery):
        if(percent_recovery >= C.num_step_lower_limit and percent_recovery <= C.num_step_upper_limit):
            return True
        else:
            C.clear()
            FTM.error_title(
                "Error: Percent recovery value is out of acceptable range!")
            return False

    @classmethod
    def packing_type_in_range_check(cls, packing_type):
        if(packing_type == 0 or packing_type == 1 or packing_type == 2):
            return True
        else:
            C.clear()
            FTM.error_title(
                "Error: Packing type value is out of acceptable range!")
            return False

    @property
    def num_step(self):
        return self.__num_step

    @num_step.setter
    def num_step(self, num_step):
        if self.num_step_in_range_check(num_step):
            self.__num_step = num_step
        else:
            return False

    @property
    def percent_recovery(self):
        return self.percent_recovery

    @percent_recovery.setter
    def percent_recovery(self, percent_recovery):
        if self.percent_recovery_in_range_check(percent_recovery):
            self.__percent_recovery = percent_recovery
        else:
            return False

    @property
    def packing_type(self):
        return self.__packing_type

    @packing_type.setter
    def packing_type(self, packing_type):
        if(packing_type == 0 or packing_type == 1 or packing_type == 2):
            pass
