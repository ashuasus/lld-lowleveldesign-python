from .db_connection_eager import DBConnectionEager
from .db_connection_lazy import DBConnectionLazy
from .db_connection_thread_safe import DBConnectionThreadSafe
from .db_connection_double_locking import DBConnectionDoubleLocking


# Test Singleton Implementation
def main():
    print("======= Singleton Design Pattern ======")

    print("====== Testing Eager Initialization ======")
    eager1 = DBConnectionEager.get_instance()
    eager2 = DBConnectionEager.get_instance()
    eager1.display_message()
    eager2.display_message()
    print("Same instance? " + str(eager1 is eager2))

    print("====== Testing Lazy Initialization ======")
    lazy1 = DBConnectionLazy.get_instance()
    lazy2 = DBConnectionLazy.get_instance()
    lazy1.display_message()
    lazy2.display_message()
    print("Same instance? " + str(lazy1 is lazy2))

    print("====== Testing Thread Safe ======")
    thread_safe1 = DBConnectionThreadSafe.get_instance()
    thread_safe2 = DBConnectionThreadSafe.get_instance()
    thread_safe1.display_message()
    thread_safe2.display_message()
    print("Same instance? " + str(thread_safe1 is thread_safe2))

    print("====== Testing Double Locking ======")
    double_locking1 = DBConnectionDoubleLocking.get_instance()
    double_locking2 = DBConnectionDoubleLocking.get_instance()
    double_locking1.display_message()
    double_locking2.display_message()
    print("Same instance? " + str(double_locking1 is double_locking2))


if __name__ == "__main__":
    main()
