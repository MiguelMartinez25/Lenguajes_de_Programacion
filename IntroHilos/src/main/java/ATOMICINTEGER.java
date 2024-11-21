import java.util.concurrent.atomic.AtomicInteger;

class InventoryAtomic {
    private final AtomicInteger stock;

    public InventoryAtomic(int initialStock) {
        this.stock = new AtomicInteger(initialStock);
    }

    public void increase(int amount) {
        stock.addAndGet(amount);
        System.out.println(Thread.currentThread().getName() + " increased stock to: " + stock.get());
    }

    public void decrease(int amount) {
        while (true) {
            int currentStock = stock.get();
            if (currentStock >= amount) {
                if (stock.compareAndSet(currentStock, currentStock - amount)) {
                    System.out.println(Thread.currentThread().getName() + " decreased stock to: " + stock.get());
                    break;
                }
            } else {
                System.out.println(Thread.currentThread().getName() + " tried to decrease stock, but not enough inventory.");
                break;
            }
        }
    }
}
