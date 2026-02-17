import { useState, useEffect } from "react";
import { Rocket } from "lucide-react";
import { Modal, Button } from "@heroui/react";

export function ModalInfo() {
  const [isOpen, setIsOpen] = useState(true);
  const [seconds, setSeconds] = useState(50);

  useEffect(() => {
    if (!isOpen) return;

    const timer = setInterval(() => {
      setSeconds((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          setIsOpen(false); // fecha automaticamente quando zerar (opcional)
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [isOpen]);

  return (
    <Modal isOpen={isOpen} onOpenChange={setIsOpen}>
      <Modal.Backdrop>
        <Modal.Container>
          <Modal.Dialog className="sm:max-w-90">
            <Modal.CloseTrigger />
            <Modal.Header>
              <Modal.Icon className="bg-default text-foreground">
                <Rocket className="size-5" />
              </Modal.Icon>
              <Modal.Heading>Olá, recrutador!</Modal.Heading>
            </Modal.Header>
            <Modal.Body>
              <p>
                Por favor, aguarde até{" "}
                <span className="font-bold text-red-500">{seconds}</span>{" "}
                segundos para primeira solicitação na API (motivo: plano free do
                Render).
              </p>
            </Modal.Body>
            <Modal.Footer>
              <Button className="w-full" onPress={() => setIsOpen(false)}>
                Continuar
              </Button>
            </Modal.Footer>
          </Modal.Dialog>
        </Modal.Container>
      </Modal.Backdrop>
    </Modal>
  );
}
