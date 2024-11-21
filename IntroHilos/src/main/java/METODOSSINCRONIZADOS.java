class InventorySynchronized {
    private int stock;

    public InventorySynchronized(int initialStock) {
        this.stock = initialStock;
    }

    public synchronized void increase(int amount) {
        stock += amount;
        System.out.println(Thread.currentThread().getName() + " increased stock to: " + stock);
    }

    public synchronized void decrease(int amount) {
        if (stock >= amount) {
            stock -= amount;
            System.out.println(Thread.currentThread().getName() + " decreased stock to: " + stock);
        } else {
            System.out.println(Thread.currentThread().getName() + " tried to decrease stock, but not enough inventory.");
        }
    }
}
