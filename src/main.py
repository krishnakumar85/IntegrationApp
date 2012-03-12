from MySteps import Parse, Fetch, Customize, GenerateInstaller
from IntegrationApp import IntegrationApp
from Process import BasicSequencer

if __name__ == "__main__":
    # Adding steps
#==============================================================================
    parsexls = Parse("Parse", "suivi_des_livraisons.xls", "v01-00-00")
    fetchdll = Fetch("Fetch", "fetch.xml")
    customize = Customize("Customize")
    generate = GenerateInstaller("Installer")

    sequence = BasicSequencer()
    sequence.add(parsexls)
    sequence.add(fetchdll)
    sequence.add(customize)
    sequence.add(generate)

    app = IntegrationApp(sequence)
    app.MainLoop()
