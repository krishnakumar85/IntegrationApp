from Process import ProcessStep
import time


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
        time.sleep(2)

    def PreCondition(self):
        print "Check if file is present"
        return 0

    def PostCondition(self):
        print "Check if build.bat is created"
        return 0


class Fetch(ProcessStep):
    def __init__(self, stepname, fetchname):
        ProcessStep.__init__(self)
        self.stepname = stepname
        self.fetchname = fetchname

    def ExecuteStep(self):
        print "Fetching DLLs"
        time.sleep(1)

    def PreCondition(self):
        print "files ready"
        return 0

    def PostCondition(self):
        print "Production folder created"
        return 0

    def Abort(self):
        print "Abort"


class Customize(ProcessStep):
    def __init__(self, stepname):
        ProcessStep.__init__(self)
        self.stepname = stepname

    def ExecuteStep(self):
        print "Customize Production"
        time.sleep(2)

    def PreCondition(self):
        print "files present"
        return 0

    def PostCondition(self):
        print "Release folder customized"
        return 0

    def Abort(self):
        print "Abort"


class GenerateInstaller(ProcessStep):
    def __init__(self, stepname):
        ProcessStep.__init__(self)
        self.stepname = stepname

    def ExecuteStep(self):
        print "Inno Setup"
        time.sleep(2)

    def PreCondition(self):
        print "iss files present"
        return 0

    def PostCondition(self):
        print "exe present"
        return 1

    def Abort(self):
        print "Abort"
