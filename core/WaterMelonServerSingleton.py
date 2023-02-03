from core.WaterMelonServer import WaterMelonServer


class WaterMelonServerSingleton:
    __instance_ptr = None

    @classmethod
    def instance(cls):
        if cls.__instance_ptr is None:
            cls.__instance_ptr = WaterMelonServer()

        return cls.__instance_ptr
