public class cuentaBancaria {

    // Recurso compartido:
    private float saldo;

    private final Object lock1 = new Object();  // Recurso de bloqueo para sincronizar

    // Constructor
    public cuentaBancaria() {
        saldo = 50000000;  // saldo inicial
    }

    // Operación de depósito (sincronizada)
    public void depositar(float valor) {
        synchronized(lock1) {
            saldo += valor;
            System.out.println("Depositado: " + valor + " | Nuevo saldo: " + saldo);
        }
    }

    // Operación de retiro (sincronizada)
    public void retirar(float valor) {
        synchronized(lock1) {
            if (saldo >= valor) {
                saldo -= valor;
                System.out.println("Retirado: " + valor + " | Nuevo saldo: " + saldo);
            } else {
                System.out.println("Saldo insuficiente para retirar: " + valor);
            }
        }
    }

    // Método para obtener el saldo
    public float getSaldo() {
        return saldo;
    }

    // Método principal
    public static void main(String[] args) {

        // Crear una cuenta bancaria
        cuentaBancaria cuenta = new cuentaBancaria();

        // Crear 3 hilos distintos, con operaciones distintas sobre la cuenta bancaria

        // Hilo 1: Depositar 10,000
        Thread hilo1 = new Thread(new Runnable() {
            @Override
            public void run() {
                cuenta.depositar(10000);
            }
        });

        // Hilo 2: Retirar 20,000
        Thread hilo2 = new Thread(new Runnable() {
            @Override
            public void run() {
                cuenta.retirar(20000);
            }
        });

        // Hilo 3: Depositar 5,000
        Thread hilo3 = new Thread(new Runnable() {
            @Override
            public void run() {
                cuenta.depositar(5000);
            }
        });

        // Iniciar los hilos
        hilo1.start();
        hilo2.start();
        hilo3.start();

        // Esperar a que terminen los hilos
        try {
            hilo1.join();
            hilo2.join();
            hilo3.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Mostrar saldo final
        System.out.println("Saldo final: " + cuenta.getSaldo());
    }
}
