from MySteps import Parse, Fetch, Customize
from IntegrationApp import IntegrationApp

if __name__ == "__main__":
    # Adding steps
    process_steps = []
    parsexls = Parse("Parse", "suivi_des_livraisons.xls", "v01-00-00")
    process_steps.append(parsexls)
    fetchdll = Fetch("Fetch", "fetch.xml")
    process_steps.append(fetchdll)
    customize = Customize("Customize")
    process_steps.append(customize)
    
    app = IntegrationApp(process_steps)
    app.MainLoop()
