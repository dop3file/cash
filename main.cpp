#include <iostream>
#include "core/storage/storage.h"

using namespace std;

int main() {
    Storage* storage = new Storage();
    storage->set("slave", new Model("123", "int"));
    cout << storage->get("slave")->get_object();
}
