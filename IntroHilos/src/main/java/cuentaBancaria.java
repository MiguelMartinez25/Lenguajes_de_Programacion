public class cuentaBancaria {

    //recurso compartido:
    private float saldo;

    private Object lock1 = new Object();

    public cuentaBancaria() {
        saldo = 50000000;
    }

    //operaciones concurrentes:
    public void depositar(float valor){
        //bloquea solo una sección de código para que solo un
        //hilo a la vez la pueda usar:
        synchronized(lock1){
            saldo += valor;
        }
    }

    public void retirar(float valor){
        saldo -= valor;
    }

    public float getSaldo(){
        return saldo;
    }

    public static void main(String[] args){
        cuentaBancaria c = new cuentaBancaria();

        //crear 3 hilos distintos, con operaciones distintas, sobre la cuenta bancaria.
        //el valor del saldo debe permanecer consistente:
        Thread hilo1 = new Thread(new Runnable() {});
    }
}
