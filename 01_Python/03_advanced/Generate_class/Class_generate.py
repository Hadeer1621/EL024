
import datetime

def generate_header_file(name , class_name , namespace):
    now = datetime.datetime.now()
    data = now.strftime("%c")
    header_content = f"""
    /****************************/
    // 
    //
    // {class_name}  header File
    // 
    // Author: {name}
    // Date: {data}
    // 
    /****************************/
    
    #ifndef {namespace}_{class_name.upper()}_H_
    #define {namespace}_{class_name.upper()}_H_

    #include <iostream>

    namespace {namespace} {{

        class {class_name} {{
        public:
            {class_name}();
            ~{class_name}();

        private:
        }};

    }}  // namespace {namespace}

    #endif  // {namespace}_{class_name.upper()}_H_
    """
    with open(f"{class_name}.h", "w") as file:
        file.write(header_content)
    
    return header_content

def generate_source_file(author,class_name,namespace):
    now = datetime.datetime.now()
    data = now.strftime("%c")
    source_content = f"""
    /****************************/
    // 
    //
    // {class_name}  Source File
    // 
    // Author: {author}
    // Date: {data}
    // 
    /****************************/
    
    #include "{class_name}.h"

    namespace {namespace} {{

        {class_name}::{class_name}() {{
            std::cout << "Constructor called for {class_name}." << std::endl;
        }}

        {class_name}::~{class_name}() {{
            std::cout << "Destructor called for {class_name}." << std::endl;
        }}

    }}  // namespace {namespace}
    """
    with open(f"{class_name}.cpp", "w") as file:
        file.write(source_content)
    
    return source_content

Author = input("Please enter the name of the author : ")
class_name = input("Please enter the name of the class : ")
namespace = input("Please enter the namespace : ")
H_file = generate_header_file(Author, class_name, namespace)
Cpp_file = generate_source_file(Author ,class_name ,namespace)

with open(f"{class_name}.h", 'w') as header_file:
   header_file.write(H_file)
  
with open(f"{class_name}.cpp", 'w') as source_file:
    source_file.write(Cpp_file)