//
// Created by Ренат Якублевич on 27.12.23.
//

#ifndef CASH_STORAGE_H
#define CASH_STORAGE_H

#include <iostream>
#include <map>
#include <any>
#include "models.h"


class Storage {
public:
    ~Storage() {

    }

    void set(std::string key, Model* value) {
        this->items[key] = value;
    }

    Model* get(std::string key) {
        if (items.count(key)) return items[key];
        return nullptr;
    }

private:
    std::map<std::string, Model*> items;
};


#endif //CASH_STORAGE_H
