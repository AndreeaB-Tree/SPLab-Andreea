from spring import TransientComponent, SingletonComponent, ClientComponent

transient_component = TransientComponent()
transient_component.operation()

singleton_component = SingletonComponent()
singleton_component.operation()


client = ClientComponent(transient_component, singleton_component)
client.operation()