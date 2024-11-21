import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class InventoryLock {
    private int stock;
    private final Lock lock = new ReentrantLock();

    public InventoryLock(int initialStock) {
        this.stock = initialStock;
    }

    public void increase(int amount) {
        lock.lock();
        try {
            stock += amount;
            System.out.println(Thread.currentThread().getName() + " increased stock to: " + stock);
        } finally {
            lock.unlock();
        }
    }

    public void decrease(int amount) {
        lock.lock();
        try {
            if (stock >= amount) {
                stock -= amount;
                System.out.println(Thread.currentThread().getName() + " decreased stock to: " + stock);
            } else {
                System.out.println(Thread.currentThread().getName() + " tried to decrease stock, but not enough inventory.");
            }
        } finally {
            lock.unlock();
        }
    }
}
