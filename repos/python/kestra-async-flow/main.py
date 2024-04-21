import os
import json
from kestra import Flow

def main():
    # Aqui você pode definir os parâmetros ou ler de um arquivo de configuração/env
    flowNamespace = os.getenv('FLOW_NAMESPACE')
    flowId = os.getenv('FLOW_ID')

    # Substitua com os parâmetros necessários para o seu flow
    flow_parameters = json.loads(os.getenv('FLOW_PARAMETERS', '{}'))

    try:
        flow = Flow()
        flow.wait_for_completion = os.getenv('WAIT_FOR_COMPLETION', 'true').lower() == 'true'
        flow.execute(flowNamespace, flowId, flow_parameters)
    except Exception as err:
        print(f"Um erro ocorreu: {err}")

if __name__ == "__main__":
    main()
