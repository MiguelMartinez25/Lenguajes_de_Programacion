import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;

public class Inventario {

    // Usamos AtomicInteger para la variable de stock
    private final AtomicInteger stock;

    // Constructor que inicializa el stock
    public Inventario(int stockInicial) {
        this.stock = new AtomicInteger(stockInicial);
    }

    // Método para ingresar productos al inventario (operación atómica)
    public void ingresar(int cantidad) {
        if (cantidad > 0) {
            // Sumamos la cantidad al stock de manera atómica
            int nuevoStock = stock.addAndGet(cantidad);
            System.out.println("Ingresados " + cantidad + " productos. Stock actual: " + nuevoStock);
        } else {
            System.out.println("Cantidad inválida para ingresar.");
        }
    }

    // Método para retirar productos del inventario (operación atómica)
    public void retirar(int cantidad) {
        if (cantidad > 0) {
            // Verificamos si el stock es suficiente
            int stockActual = stock.get();
            if (stockActual >= cantidad) {
                // Decrementamos la cantidad de productos de manera atómica
                int nuevoStock = stock.addAndGet(-cantidad);
                System.out.println("Retirados " + cantidad + " productos. Stock restante: " + nuevoStock);
            } else {
                System.out.println("No hay suficiente stock para retirar " + cantidad + " productos.");
            }
        } else {
            System.out.println("Cantidad inválida para retirar.");
        }
    }

    // Método para obtener el stock actual (lectura atómica)
    public int getStock() {
        return stock.get();  // Operación atómica de lectura
    }

    // Método principal con la interacción con el usuario
    public static void main(String[] args) {

        // Crear un inventario con 100 productos iniciales
        Inventario inventario = new Inventario(10);
        Scanner scanner = new Scanner(System.in);

        while (true) {
            // Mostrar el menú de opciones
            System.out.println("\n*** Menú de Inventario ***");
            System.out.println("1. Ingresar productos");
            System.out.println("2. Retirar productos");
            System.out.println("3. Ver stock actual");
            System.out.println("4. Salir");
            System.out.print("Elige una opción (1-4): ");

            // Leer la opción del usuario
            int opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    // Ingresar productos
                    System.out.print("¿Cuántos productos deseas ingresar? ");
                    int cantidadIngresar = scanner.nextInt();
                    inventario.ingresar(cantidadIngresar);
                    break;

                case 2:
                    // Retirar productos
                    System.out.print("¿Cuántos productos deseas retirar? ");
                    int cantidadRetirar = scanner.nextInt();
                    inventario.retirar(cantidadRetirar);
                    break;

                case 3:
                    // Mostrar el stock actual
                    System.out.println("Stock actual: " + inventario.getStock());
                    break;

                case 4:
                    // Salir del programa
                    System.out.println("¡Gracias por usar el sistema de inventario!");
                    scanner.close();
                    return; // Salir del programa

                default:
                    System.out.println("Opción inválida, vuelve a intentarlo");
            }
        }
    }
}
