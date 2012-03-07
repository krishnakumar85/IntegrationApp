from MySteps import Parse, Fetch
from IntegrationApp import IntegrationApp

if __name__ == "__main__":
    # Adding steps
    process_steps = []
    parsexls = Parse("Parse", "suivi_des_livraisons.xls", "v01-00-00")
    process_steps.append(parsexls)
    fetchdll = Fetch("Fetch", "fetch.xml")
    process_steps.append(fetchdll)

    app = IntegrationApp(process_steps)
    app.MainLoop()
