import { Button } from "@heroui/react";
import { Github } from "lucide-react";

export default function AppNavbar() {
  return (
    <nav className="flex items-center justify-between px-4 md:px-6 py-3 md:py-4 border-b">
      <p className="font-light text-base md:text-xl">Desafio Clarke Energia</p>
      <Button
        color="primary"
        variant="flat"
        size="sm"
        className="md:size-md"
        onPress={() =>
          window.open(
            "https://github.com/jrcarls/desafio-clarkeenergia",
            "_blank",
          )
        }
      >
        <Github className="w-4 h-4 md:hidden" />
        <span className="hidden md:inline">Repositório no GitHub</span>
      </Button>
    </nav>
  );
}
