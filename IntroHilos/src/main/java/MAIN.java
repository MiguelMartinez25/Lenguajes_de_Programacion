public class InventoryTest {
    public static void main(String[] args) {
        // Cambia la clase según el método que quieras probar.
        InventorySynchronized inventory = new InventorySynchronized(50);

        Runnable task = () -> {
            for (int i = 0; i < 5; i++) {
                inventory.increase(10);
                inventory.decrease(15);
            }
        };

        Thread t1 = new Thread(task, "Thread-1");
        Thread t2 = new Thread(task, "Thread-2");

        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
