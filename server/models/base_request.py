
class BaseRequest:
    def __init__(self, request_params: dict):
        self.data = {}
        self.module_attrs = vars(self.__class__)["__annotations__"]
        self.process_attrs(request_params)

    
    def process_attrs(self, req_pars: dict):
        r"""Process and validate all request params and types
        with respect to their correspond class atributes.
        Sopprted types are: `int`, `float`, `str`, `list` and `dict`
        """
        if req_pars.keys() == self.module_attrs.keys():
            for k, converter in self.module_attrs.items():
                try:
                    self.data[k] = converter(req_pars[k])
                except:
                    #print(type(req_pars[k]), type(converter))
                    if type(req_pars[k]) == type(converter):
                        self.data[k] = req_pars[k]
                    else:
                        self.data = {}
                        return
                #print(k, req_pars[k])
    
    
    def asdict(self):
        return self.data

    def getObject(self):
        if self.data == {}:
            return None
        return self.data
    
    # def __dict__(self): return 