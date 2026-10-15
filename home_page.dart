import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Homepage"),
        // centerTitle: true,
        backgroundColor: Colors.blue,
        foregroundColor: Colors.white,
        // leading: Icon(Icons.home),
        actions: [
          IconButton(
            tooltip: "Search",
            onPressed: () {},
            icon: Icon(Icons.search),
          ),
          IconButton(
            tooltip: "Person",
            onPressed: () {},
            icon: Icon(Icons.person),
          ),
          IconButton(
            tooltip: "Settings",
            onPressed: () {},
            icon: Icon(Icons.settings),
          ),

          IconButton(
            tooltip: "Delete",
            onPressed: () {},
            icon: Icon(Icons.delete),
          ),
        ],
      ),
      drawer: Drawer(
        child: Column(
          children: [
            UserAccountsDrawerHeader(
              accountName: Text("Shuvon"),
              accountEmail: Text("shuvon@gmail.com"),
              decoration: BoxDecoration(color: Colors.blue),
            ),
            ListTile(
              title: Text("Homepage"),

              leading: Icon(Icons.home),
              hoverColor: Colors.grey,
              onTap: () {},
            ),

            Spacer(),
            // Divider(),

            ListTile(
              title: Text("Profile"),
              leading: Icon(Icons.person),
              hoverColor: Colors.pink[100],
              onTap: () {},
            ),
          ],
        ),
      ),

      body: SingleChildScrollView(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(10),
              child: Row(
                children: [
                  TextButton(
                    onPressed: () {},
                    style: TextButton.styleFrom(
                      backgroundColor: Colors.green,
                      foregroundColor: Colors.white,
                      fixedSize: Size(100, 100),
                      side: BorderSide(),
                      elevation: 10,
                    ),
                    child: Text("TextButton"),
                  ),
                  SizedBox(width: 10),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: ElevatedButton(
                      onPressed: () {},
                      style: ElevatedButton.styleFrom(
                        backgroundColor: const Color.fromARGB(
                          255,
                          215,
                          129,
                          230,
                        ),
                        foregroundColor: Colors.white,
                        fixedSize: Size(150, 20),
                        side: BorderSide(),
                      ),
                      child: Text("ElevatedButton"),
                    ),
                  ),

                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: OutlinedButton(
                      onPressed: () {},
                      child: Text("OutlinedButton"),
                    ),
                  ),
                  IconButton(
                    onPressed: () {},
                    style: IconButton.styleFrom(backgroundColor: Colors.yellow),
                    icon: Icon(Icons.login),
                  ),
                ],
              ),
            ),

            Container(
              height: 200,
              width: 200,
              padding: EdgeInsets.all(30),
              margin: EdgeInsets.all(20),
              alignment: Alignment.bottomRight,
              decoration: BoxDecoration(
                color: Colors.purple,
                border: Border.all(width: 5, color: Colors.black),

                borderRadius: BorderRadius.all(Radius.circular(20)),
                gradient: RadialGradient(colors: [Colors.red, Colors.green]),
              ),
              child: Text("Hello container"),
            ),
            SizedBox(
              height: 800,
              width: 200,
              child: Card(
                margin: EdgeInsets.all(20),
                color: Colors.blue,
                shadowColor: Colors.red,
                elevation: 50,
                //shape: (),
                child: Center(child: Text("Hello Card,shuvon")),
              ),
            ),

            Image.asset('assets/images/Screenshot.png'),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        tooltip: "Add",
        backgroundColor: Colors.grey,
        foregroundColor: Colors.white,

        child: Icon(Icons.add),
      ),
    );
  }
}
