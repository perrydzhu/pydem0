from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("An apple a day keeps the doctor away")
        self.transport.loseConnection()


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:8888").listen(EchoFactory())
reactor.run()