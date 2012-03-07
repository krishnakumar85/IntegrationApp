from Process import ProcessStep


class Cleanup(ProcessStep):
    pass


class Parse(ProcessStep):
    def __init__(self, stepname, filename, version):
        ProcessStep.__init__(self)

        self.stepname = stepname
        self.filename = filename
        self.version = version

    def ExecuteStep(self):
        print "Parsing file"

    def PreCondition(self):
        print "Check if file is present"
        return 1

    def PostCondition(self):
        print "Check if build.bat is created"


class Fetch(ProcessStep):
    def __init__(self, stepname, fetchname):
        ProcessStep.__init__(self)
        self.stepname = stepname
        self.fetchname = fetchname

    def ExecuteStep(self):
        print "Fetching DLLs"

    def PreCondition(self):
        print "files ready"
        return 0

    def PostCondition(self):
        print "Production folder created"
        return 1

    def Abort(self):
        print "Abort"
