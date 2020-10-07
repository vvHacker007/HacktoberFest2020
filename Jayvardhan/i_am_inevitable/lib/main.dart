import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        title: Text("I AM INEVITABLE"),
        backgroundColor: Colors.purple,
      ),
      body: Center(
        child: Image(
            image: NetworkImage(
                "https://fsb.zobj.net/crop.php?r=pWuk_xgLXYqZdGDLRiHN6FelVkqRrMEfMkP0U8CJR3t-hHKW48d_RAdoWhkBmd4dmCIN2FoZhiDiVjObZBAx-_25e_2jnEgmrXwPQl14JktYCvMNzdCuCFuV0BorhATe5QcNi604Mg0fJ6s0")),
      ),
    ),
  ));
}
