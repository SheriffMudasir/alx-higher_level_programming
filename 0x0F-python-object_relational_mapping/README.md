 **Project: 0x0F. Python - Object-relational mapping**

This repository contains a collection of Python scripts demonstrating Object-Relational Mapping (ORM) using SQLAlchemy. The scripts cover various tasks related to creating, querying, and modifying database tables using SQLAlchemy and MySQL.

### Files:

1. **[0-select_states.py](0x0F-python-object_relational_mapping/0-select_states.py):**
   - Lists all states from the database hbtn_0e_0_usa.
   - Takes MySQL username, password, and database name as arguments.

2. **[1-filter_states.py](0x0F-python-object_relational_mapping/1-filter_states.py):**
   - Lists all states with a name starting with 'N' (upper N) from the database hbtn_0e_0_usa.
   - Takes MySQL username, password, and database name as arguments.

3. **[2-my_filter_states.py](0x0F-python-object_relational_mapping/2-my_filter_states.py):**
   - Displays all values in the states table of hbtn_0e_0_usa where the name matches the argument.
   - Takes MySQL username, password, database name, and state name as arguments.

4. **[3-my_safe_filter_states.py](0x0F-python-object_relational_mapping/3-my_safe_filter_states.py):**
   - Displays all values in the states table of hbtn_0e_0_usa where the name matches the argument, safe from MySQL injections.
   - Takes MySQL username, password, database name, and state name as arguments.

5. **[4-cities_by_state.py](0x0F-python-object_relational_mapping/4-cities_by_state.py):**
   - Lists all cities from the database hbtn_0e_4_usa.
   - Takes MySQL username, password, and database name as arguments.

6. **[5-filter_cities.py](0x0F-python-object_relational_mapping/5-filter_cities.py):**
   - Lists all cities of a given state from the database hbtn_0e_4_usa.
   - Takes MySQL username, password, database name, and state name as arguments.

7. **[6-model_state.py](0x0F-python-object_relational_mapping/6-model_state.py):**
   - Defines a `State` class with attributes and links it to a MySQL table using SQLAlchemy.
   - The script connects to a MySQL server and creates the corresponding table.

8. **[7-model_state_fetch_all.py](0x0F-python-object_relational_mapping/7-model_state_fetch_all.py):**
   - Lists all `State` objects from the database hbtn_0e_6_usa.
   - Takes MySQL username, password, and database name as arguments.

9. **[8-model_state_fetch_first.py](0x0F-python-object_relational_mapping/8-model_state_fetch_first.py):**
   - Prints the first `State` object from the database hbtn_0e_6_usa.
   - Takes MySQL username, password, and database name as arguments.

10. **[9-model_state_filter_a.py](0x0F-python-object_relational_mapping/9-model_state_filter_a.py):**
    - Lists all `State` objects containing the letter 'a' from the database hbtn_0e_6_usa.
    - Takes MySQL username, password, and database name as arguments.

11. **[10-model_state_my_get.py](0x0F-python-object_relational_mapping/10-model_state_my_get.py):**
    - Prints the `State` object with the name passed as an argument from the database hbtn_0e_6_usa.
    - Takes MySQL username, password, database name, and state name as arguments.

12. **[11-model_state_insert.py](0x0F-python-object_relational_mapping/11-model_state_insert.py):**
    - Adds the `State` object "Louisiana" to the database hbtn_0e_6_usa.
    - Takes MySQL username, password, and database name as arguments.

13. **[12-model_state_update_id_2.py](0x0F-python-object_relational_mapping/12-model_state_update_id_2.py):**
    - Changes the name of a `State` object with id=2 to "New Mexico" in the database hbtn_0e_6_usa.
    - Takes MySQL username, password, and database name as arguments.

14. **[13-model_state_delete_a.py](0x0F-python-object_relational_mapping/13-model_state_delete_a.py):**
    - Deletes all `State` objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
    - Takes MySQL username, password, and database name as arguments.

15. **[model_city.py](0x0F-python-object_relational_mapping/model_city.py):**
   

 - Defines a `City` class with attributes and links it to a MySQL table using SQLAlchemy.
    - No change compared to `model_state.py`.

16. **[14-model_city_fetch_by_state.py](0x0F-python-object_relational_mapping/14-model_city_fetch_by_state.py):**
    - Prints all `City` objects from the database hbtn_0e_14_usa sorted by state.
    - Takes MySQL username, password, and database name as arguments.

17. **[relationship_city.py](0x0F-python-object_relational_mapping/relationship_city.py):**
    - Improves the `model_city.py` file by adding a foreign key relationship with the `states` table.
    - Defines the `City` class with the new relationship.

18. **[relationship_state.py](0x0F-python-object_relational_mapping/relationship_state.py):**
    - Improves the `model_state.py` file by adding a relationship with the `City` class.
    - Defines the `State` class with the new relationship.

19. **[100-relationship_states_cities.py](0x0F-python-object_relational_mapping/100-relationship_states_cities.py):**
    - Creates the State "California" with the City "San Francisco" in the database hbtn_0e_100_usa.
    - Takes MySQL username, password, and database name as arguments.
    - Utilizes the relationship feature for all `State` objects.

### How to Run:

- To execute any script, provide the required command-line arguments. For example:
  ```bash
  ./script_name.py username password database_name
  ```

### Prerequisites:

- Ensure that you have the necessary Python libraries installed, especially SQLAlchemy.
- A MySQL server running on localhost at port 3306 is required for script execution.