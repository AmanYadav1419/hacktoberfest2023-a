import aiml
import os


def chat():
    kernel = aiml.Kernel()
    kernel.verbose(0)
    kernel.setBotPredicate("name", "Nicole")
    kernel.setPredicate('name', 'Raj')

    if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile="bot_brain.brn")
    else:
        kernel.bootstrap(learnFiles="startup.xml", commands="LOAD AIML B")
        kernel.saveBrain("bot_brain.brn")

    print("Session Initiated. Type your message.")
    while True:
        excitation = input('')
        response = kernel.respond(excitation)
        if excitation in ['EXIT', 'exit', 'Exit']:
            break
        print(f'>>> {response}')
        kernel.saveBrain("bot_brain.brn")
    print("Session Ended")


if __name__ == '__main__':
    chat()