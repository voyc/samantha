#!/usr/bin/env python

# https://gist.github.com/dankrause/9607475

#   Copyright 2017 Dan Krause
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

""" ipc_example.py
Usage:
    ipc_example.py server [options]
    ipc_example.py client [options] <class> [--arg=<arg>...] [--kwarg=<kwarg>...]

Options:
    -p --port=<port>      The port number to communicate over [default: 5795]
    -h --host=<host>      The host name to communicate over [default: localhost]
    -s --socket=<socket>  A socket file to use, instead of a host:port
    -a --arg=<arg>        A positional arg to supply the class constructor
    -k --kwarg=<kwarg>    A keyword arg to supply the class constructor
"""

import docopt
import ipc


class Event(ipc.Message):
    def __init__(self, event_type, **properties):
        self.type = event_type
        self.properties = properties

    def _get_args(self):
        return [self.type], self.properties


class Response(ipc.Message):
    def __init__(self, text):
        self.text = text

    def _get_args(self):
        return [self.text], {}


def server_process_request(objects):
    response = [Response('Received {} objects'.format(len(objects)))]
    print( 'Received objects: {}'.format(objects))
    print( 'Sent objects: {}'.format(response))
    return response


if __name__ == '__main__':
    print(__doc__)
    args = docopt.docopt(__doc__)
    server_address = args['--socket'] or (args['--host'], int(args['--port']))
    print(server_address)

    if args['server']:
        ipc.Server(server_address, server_process_request).serve_forever()

    if args['client']:
        kwargs = {k: v for k, v in [i.split('=', 1) for i in args['--kwarg']]}
        user_input = [{'class': args['<class>'], 'args': args['--arg'], 'kwargs': kwargs}]
        objects = ipc.Message.deserialize(user_input)
        print( 'Sending objects: {}'.format(objects))
        with ipc.Client(server_address) as client:
            response = client.send(objects)
        print( 'Received objects: {}'.format(response))


# Example usage:
#     $ ./ipc_example.py server
#     then in another terminal:
#     $ ./ipc_example.py client Event --arg=testevent --kwarg=exampleproperty=examplevalue
