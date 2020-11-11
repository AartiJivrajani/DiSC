class Node:
    def __init__(self, node_id, protocol, np, adversary=False):
        self.id = node_id
        self.received_messages = []
        self.committed_log = []
        self.protocol = protocol
        self.np = np
        self.adversary = adversary
        
    def get_id(self):
        return self.id

    def run_protocol_one_round(self):
        # store messages in local memory
        self.received_messages = []
        self.received_messages = self.np.receive_messages(self.get_id())
        
        # run protocol with stored messages
        send_messages = self.protocol.run(self.received_messages)
        
        # send messages from protocol (protocol returns an array of messages to send?)
        for i in range(self.np.num_nodes):
            self.np.send_message(self.get_id(), i, send_messages[i])
    
    def get_committed_log(self):
        return self.committed_log

    def adversary_actions(self):
        # stub
        pass
