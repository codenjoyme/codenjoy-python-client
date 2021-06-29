This project represents a basic python websocket client for the codenjoy platform.
It allows you to easily and quickly join the game, developing your unique algorithm, having a configured infrastructure.

# What do you need to get started?
To get started, you should define the desired game and enter a value in `main.game`. \
The second important thing is the connection token to the server. After successful authorization on the site, you must copy the url
and enter a value in `main.url`. \
This is enough to connect and participate in the competition.

# How to run it?
The entry point for starting a project is `main()` func in `main.py`. \
You can pass the game type and token connection to the server as command-line arguments.
Game parameters passed by arguments at startup have a higher priority than those defined in the code.

The archive is run with the command `python3 main.py [<game>] [<url>]`

# How does it work?
The elements on the map are defined in `games/<gamename>/element.py`. They determine the meaning of a particular symbol.
The two important components of the game are the `games/<gamename>/board.[py]` game board
and the `games/<gamename>/solver.py` solver.

Every second the server sends a string representation of the current state of the board, which is parsed in an object of class `Board`.
Then the server expects a string representation of your bot's action that is computed by executing `Solver.get(board_string)`.

Using the set of available methods of the `Board` class, you improve the algorithm of the bot's behavior.
You should develop this class, extending it with new methods that will be your tool in the fight.
For example, a bot can get information about an element in a specific coordinate by calling `AbstractBoard.get_at(x, y)`
or count the number of elements of a certain type near the coordinate by calling `AbstractBoard.cout_near(x, y, elem)`, etc.

# Business logic testing
Writing tests will allow you to create conclusive evidence of the correctness of the existing code.
This is your faithful friend, who is always ready to answer the question: "Is everything working as I expect? The new code did not break my existing logic?". \
The `tests/abstract_board.py` file contains a set of tests that check board tools.
Implementation of new methods should be accompanied by writing new tests and checking the results of processing existing ones. \
Use `tests/games/<gamename>/solver.py` to check the bot's behavior for a specific game scenario.