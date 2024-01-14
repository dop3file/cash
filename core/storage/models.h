//
// Created by Ренат Якублевич on 27.12.23.
//

#ifndef CASH_MODELS_H
#define CASH_MODELS_H

#include <iostream>
#include <typeinfo>

class TypeValidator {
public:
    bool IsNumeric(const std::string& str) {
        try {
            std::size_t pos = 0;
            std::stoi(str, &pos);
            return pos == str.length();
        } catch (...) {
            return false;
        }
    }

    void router(std::string object, std::string type) {
        if (type == "int" && !IsNumeric(object)) {
            throw std::runtime_error("error");
        }
        throw std::runtime_error("error");
    }
};

class Model {
public:
    Model() {
        this->object = nullptr;
        this->type = "";
    }

    Model(std::string object, std::string type) {
        this->object = object;
        this->type = type;
//        validate_type();
    }

    std::string get_object() {
        return object;
    }

    void validate_type() {
        TypeValidator validator;
        try {
            validator.router(object, type);
        } catch(...) {
            throw std::runtime_error("error");
        }
    }

private:
    std::string object;
    std::string type;
};


#endif //CASH_MODELS_H
