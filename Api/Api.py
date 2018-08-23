from Api.deparments_api import DeparmentsApi


class GetApis(object):

    def get_department_api(self):
        return DeparmentsApi()
